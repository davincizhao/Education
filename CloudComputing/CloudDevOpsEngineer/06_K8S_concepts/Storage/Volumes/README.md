# Volumes
On-disk files in a container are ephemeral, which presents some problems for non-trivial applications when running in containers. One problem is the loss of files when a container crashes. The kubelet restarts the container but with a clean state. A second problem occurs when sharing files between containers running together in a Pod. The Kubernetes volume abstraction solves both of these problems. Familiarity with Pods is suggested.

## Background

Docker has a concept of volumes, though it is somewhat looser and less managed. A Docker volume is a directory on disk or in another container. Docker provides volume drivers, but the functionality is somewhat limited.

Kubernetes supports many types of volumes. A Pod can use any number of volume types simultaneously. Ephemeral volume types have a lifetime of a pod, but persistent volumes exist beyond the lifetime of a pod. When a pod ceases to exist, Kubernetes destroys ephemeral volumes; however, Kubernetes does not destroy persistent volumes. For any kind of volume in a given pod, data is preserved across container restarts.

At its core, a volume is a directory, possibly with some data in it, which is accessible to the containers in a pod. How that directory comes to be, the medium that backs it, and the contents of it are determined by the particular volume type used.

To use a volume, specify the volumes to provide for the Pod in ```.spec.volumes``` and declare where to mount those volumes into containers in ```.spec.containers[*].volumeMounts```. A process in a container sees a filesystem view composed from the initial contents of the container image, plus volumes (if defined) mounted inside the container. The process sees a root filesystem that initially matches the contents of the container image. Any writes to within that filesystem hierarchy, if allowed, affect what that process views when it performs a subsequent filesystem access. Volumes mount at the specified paths within the image. For each container defined within a Pod, you must independently specify where to mount each volume that the container uses.

**Note:** Volumes cannot mount within other volumes (but see Using subPath for a related mechanism). Also, a volume cannot contain a hard link to anything in a different volume.

## Types of Volumes

Kubernetes supports several types of volumes.

### awsElasticBlockStore
An ```awsElasticBlockStore``` volume mounts an Amazon Web Services (AWS) EBS volume into your pod. Unlike ```emptyDir```, which is erased when a pod is removed, the contents of an EBS volume are persisted and the volume is unmounted. This means that an EBS volume can be pre-populated with data, and that data can be shared between pods.

**Note:** You must create an EBS volume by using aws ec2 create-volume or the AWS API before you can use it.
There are some restrictions when using an ```awsElasticBlockStore``` volume:

- the nodes on which pods are running must be AWS EC2 instances
- those instances need to be in the same region and availability zone as the EBS volume
- EBS only supports a single EC2 instance mounting a volume

### Creating an AWS EBS volume
Before you can use an EBS volume with a pod, you need to create it.
```
aws ec2 create-volume --availability-zone=eu-west-1a --size=10 --volume-type=gp2
```
Make sure the zone matches the zone you brought up your cluster in. Check that the size and EBS volume type are suitable for your use.

### AWS EBS configuration example
```
apiVersion: v1
kind: Pod
metadata:
  name: test-ebs
spec:
  containers:
  - image: k8s.gcr.io/test-webserver
    name: test-container
    volumeMounts:
    - mountPath: /test-ebs
      name: test-volume
  volumes:
  - name: test-volume
    # This AWS EBS volume must already exist.
    awsElasticBlockStore:
      volumeID: "<volume id>"
      fsType: ext4
```

If the EBS volume is partitioned, you can supply the optional field partition: "<partition number>" to specify which parition to mount on.

### configMap
A ConfigMap provides a way to inject configuration data into pods. The data stored in a ConfigMap can be referenced in a volume of type ```configMap``` and then consumed by containerized applications running in a pod.

When referencing a ConfigMap, you provide the name of the ConfigMap in the volume. You can customize the path to use for a specific entry in the ConfigMap. The following configuration shows how to mount the ```log-config``` ConfigMap onto a Pod called ```configmap-pod```:
```
apiVersion: v1
kind: Pod
metadata:
  name: configmap-pod
spec:
  containers:
    - name: test
      image: busybox
      volumeMounts:
        - name: config-vol
          mountPath: /etc/config
  volumes:
    - name: config-vol
      configMap:
        name: log-config
        items:
          - key: log_level
            path: log_level
            
```            
The ```log-config``` ConfigMap is mounted as a volume, and all contents stored in its log_level entry are mounted into the Pod at path ```/etc/config/log_level```. Note that this path is derived from the volume's mountPath and the path keyed with ```log_level```.

**Note:**
- You must create a ConfigMap before you can use it.

- A container using a ConfigMap as a subPath volume mount will not receive ConfigMap updates.

- Text data is exposed as files using the UTF-8 character encoding. For other character encodings, use binaryData.

### downwardAPI 
A ```downwardAPI``` volume makes downward API data available to applications. It mounts a directory and writes the requested data in plain text files.

**Note:** A container using the downward API as a subPath volume mount will not receive downward API updates.

### emptyDir
An ```emptyDir``` volume is first created when a Pod is assigned to a node, and exists as long as that Pod is running on that node. As the name says, the emptyDir volume is initially empty. All containers in the Pod can read and write the same files in the ```emptyDir``` volume, though that volume can be mounted at the same or different paths in each container. When a Pod is removed from a node for any reason, the data in the ```emptyDir``` is deleted permanently.

**Note:** A container crashing does not remove a Pod from a node. The data in an emptyDir volume is safe across container crashes.


Some uses for an emptyDir are:

- scratch space, such as for a disk-based merge sort
- checkpointing a long computation for recovery from crashes
- holding files that a content-manager container fetches while a webserver container serves the data

Depending on your environment, ```emptyDir``` volumes are stored on whatever medium that backs the node such as disk or SSD, or network storage. However, if you set the ```emptyDir.medium``` field to ```"Memory"```, Kubernetes mounts a tmpfs (RAM-backed filesystem) for you instead. While tmpfs is very fast, be aware that unlike disks, tmpfs is cleared on node reboot and any files you write count against your container's memory limit.

**Note:** If the SizeMemoryBackedVolumes feature gate is enabled, you can specify a size for memory backed volumes. If no size is specified, memory backed volumes are sized to 50% of the memory on a Linux host.

### emptyDir configuration example 
```
apiVersion: v1
kind: Pod
metadata:
  name: test-pd
spec:
  containers:
  - image: k8s.gcr.io/test-webserver
    name: test-container
    volumeMounts:
    - mountPath: /cache
      name: cache-volume
  volumes:
  - name: cache-volume
    emptyDir: {}
```
### fc (fibre channel) 
An fc volume type allows an existing fibre channel block storage volume to mount in a Pod. You can specify single or multiple target world wide names (WWNs) using the parameter targetWWNs in your Volume configuration. If multiple WWNs are specified, targetWWNs expect that those WWNs are from multi-path connections

### hostPath

**Warning:**
HostPath volumes present many security risks, and it is a best practice to avoid the use of HostPaths when possible. When a HostPath volume must be used, it should be scoped to only the required file or directory, and mounted as ReadOnly.

If restricting HostPath access to specific directories through AdmissionPolicy, ```volumeMounts``` MUST be required to use ```readOnly``` mounts for the policy to be effective.

A ```hostPath``` volume mounts a file or directory from the host node's filesystem into your Pod. This is not something that most Pods will need, but it offers a powerful escape hatch for some applications.

For example, some uses for a hostPath are:

- running a container that needs access to Docker internals; use a hostPath of /var/lib/docker
- running cAdvisor in a container; use a hostPath of /sys
- allowing a Pod to specify whether a given hostPath should exist prior to the Pod running, whether it should be created, and what it should exist as

In addition to the required ```path``` property, you can optionally specify a ```type``` for a ```hostPath``` volume.

The supported values for field ```type``` are:
```
**Value	                                     Behavior**
- Empty string (default) is for backward compatibility, which means that no checks will be performed before mounting the hostPath volume.
- DirectoryOrCreate	If nothing exists at the given path, an empty directory will be created there as needed with permission set to 0755, having the same group and ownership with Kubelet.
- Directory	A directory must exist at the given path
- FileOrCreate	If nothing exists at the given path, an empty file will be created there as needed with permission set to 0644, having the same group and ownership with Kubelet.
- File	A file must exist at the given path
- Socket	A UNIX socket must exist at the given path
- CharDevice	A character device must exist at the given path
- BlockDevice	A block device must exist at the given path

```
Watch out when using this type of volume, because:

- HostPaths can expose privileged system credentials (such as for the Kubelet) or privileged APIs (such as container runtime socket), which can be used for container escape or to attack other parts of the cluster.
- Pods with identical configuration (such as created from a PodTemplate) may behave differently on different nodes due to different files on the nodes
- The files or directories created on the underlying hosts are only writable by root. You either need to run your process as root in a privileged Container or modify the file permissions on the host to be able to write to a hostPath volume

### hostPath configuration example
```
apiVersion: v1
kind: Pod
metadata:
  name: test-pd
spec:
  containers:
  - image: k8s.gcr.io/test-webserver
    name: test-container
    volumeMounts:
    - mountPath: /test-pd
      name: test-volume
  volumes:
  - name: test-volume
    hostPath:
      # directory location on host
      path: /data
      # this field is optional
      type: Directory
```

**Caution:** The FileOrCreate mode does not create the parent directory of the file. If the parent directory of the mounted file does not exist, the pod fails to start. To ensure that this mode works, you can try to mount directories and files separately, as shown in the FileOrCreateconfiguration.

### hostPath FileOrCreate configuration example
```
apiVersion: v1
kind: Pod
metadata:
  name: test-webserver
spec:
  containers:
  - name: test-webserver
    image: k8s.gcr.io/test-webserver:latest
    volumeMounts:
    - mountPath: /var/local/aaa
      name: mydir
    - mountPath: /var/local/aaa/1.txt
      name: myfile
  volumes:
  - name: mydir
    hostPath:
      # Ensure the file directory is created.
      path: /var/local/aaa
      type: DirectoryOrCreate
  - name: myfile
    hostPath:
      path: /var/local/aaa/1.txt
      type: FileOrCreate
```

### iscsi
An ```iscsi``` volume allows an existing iSCSI (SCSI over IP) volume to be mounted into your Pod. Unlike ```emptyDir```, which is erased when a Pod is removed, the contents of an iscsi volume are preserved and the volume is merely unmounted. This means that an iscsi volume can be pre-populated with data, and that data can be shared between pods.

**Note:** You must have your own iSCSI server running with the volume created before you can use it.
A feature of iSCSI is that it can be mounted as read-only by multiple consumers simultaneously. This means that you can pre-populate a volume with your dataset and then serve it in parallel from as many Pods as you need. Unfortunately, iSCSI volumes can only be mounted by a single consumer in read-write mode. Simultaneous writers are not allowed.

### local
A ```local``` volume represents a mounted local storage device such as a disk, partition or directory.

Local volumes can only be used as a statically created PersistentVolume. Dynamic provisioning is not supported.

Compared to ```hostPath``` volumes, ```local``` volumes are used in a durable and portable manner without manually scheduling pods to nodes. The system is aware of the volume's node constraints by looking at the node affinity on the PersistentVolume.

However, ```local``` volumes are subject to the availability of the underlying node and are not suitable for all applications. If a node becomes unhealthy, then the local volume becomes inaccessible by the pod. The pod using this volume is unable to run. Applications using ```local``` volumes must be able to tolerate this reduced availability, as well as potential data loss, depending on the durability characteristics of the underlying disk.

The following example shows a PersistentVolume using a ```local``` volume and ```nodeAffinity```:
```
apiVersion: v1
kind: PersistentVolume
metadata:
  name: example-pv
spec:
  capacity:
    storage: 100Gi
  volumeMode: Filesystem
  accessModes:
  - ReadWriteOnce
  persistentVolumeReclaimPolicy: Delete
  storageClassName: local-storage
  local:
    path: /mnt/disks/ssd1
  nodeAffinity:
    required:
      nodeSelectorTerms:
      - matchExpressions:
        - key: kubernetes.io/hostname
          operator: In
          values:
          - example-node
```
You must set a PersistentVolume nodeAffinity when using local volumes. The Kubernetes scheduler uses the PersistentVolume nodeAffinity to schedule these Pods to the correct node.

PersistentVolume volumeMode can be set to "Block" (instead of the default value "Filesystem") to expose the local volume as a raw block device.

When using local volumes, it is recommended to create a StorageClass with volumeBindingMode set to WaitForFirstConsumer. For more details, see the local StorageClass example. Delaying volume binding ensures that the PersistentVolumeClaim binding decision will also be evaluated with any other node constraints the Pod may have, such as node resource requirements, node selectors, Pod affinity, and Pod anti-affinity.

An external static provisioner can be run separately for improved management of the local volume lifecycle. Note that this provisioner does not support dynamic provisioning yet. For an example on how to run an external local provisioner, see the local volume provisioner user guide.

Note: The local PersistentVolume requires manual cleanup and deletion by the user if the external static provisioner is not used to manage the volume lifecycle.
### nfs

An nfs volume allows an existing NFS (Network File System) share to be mounted into a Pod. Unlike emptyDir, which is erased when a Pod is removed, the contents of an nfs volume are preserved and the volume is merely unmounted. This means that an NFS volume can be pre-populated with data, and that data can be shared between pods. NFS can be mounted by multiple writers simultaneously.

**Note:** You must have your own NFS server running with the share exported before you can use it.

### persistentVolumeClaim 
A ```persistentVolumeClaim``` volume is used to mount a PersistentVolume into a Pod. PersistentVolumeClaims are a way for users to "claim" durable storage (such as a GCE PersistentDisk or an iSCSI volume) without knowing the details of the particular cloud environment.

See the information about PersistentVolumes for more details.

### portworxVolume

A ```portworxVolume``` is an elastic block storage layer that runs hyperconverged with Kubernetes. Portworx fingerprints storage in a server, tiers based on capabilities, and aggregates capacity across multiple servers. Portworx runs in-guest in virtual machines or on bare metal Linux nodes.

A portworxVolume can be dynamically created through Kubernetes or it can also be pre-provisioned and referenced inside a Pod. Here is an example Pod referencing a pre-provisioned Portworx volume:
```
apiVersion: v1
kind: Pod
metadata:
  name: test-portworx-volume-pod
spec:
  containers:
  - image: k8s.gcr.io/test-webserver
    name: test-container
    volumeMounts:
    - mountPath: /mnt
      name: pxvol
  volumes:
  - name: pxvol
    # This Portworx volume must already exist.
    portworxVolume:
      volumeID: "pxvol"
      fsType: "<fs-type>"
```

### projected
A projected volume maps several existing volume sources into the same directory. For more details, see projected volumes.

### secret 
A secret volume is used to pass sensitive information, such as passwords, to Pods. You can store secrets in the Kubernetes API and mount them as files for use by pods without coupling to Kubernetes directly. secret volumes are backed by tmpfs (a RAM-backed filesystem) so they are never written to non-volatile storage.

## Using subPath
Sometimes, it is useful to share one volume for multiple uses in a single pod. The ```volumeMounts.subPath``` property specifies a sub-path inside the referenced volume instead of its root.

The following example shows how to configure a Pod with a LAMP stack (Linux Apache MySQL PHP) using a single, shared volume. This sample subPath configuration is not recommended for production use.

The PHP application's code and assets map to the volume's html folder and the MySQL database is stored in the volume's mysql folder. For example:
```
apiVersion: v1
kind: Pod
metadata:
  name: my-lamp-site
spec:
    containers:
    - name: mysql
      image: mysql
      env:
      - name: MYSQL_ROOT_PASSWORD
        value: "rootpasswd"
      volumeMounts:
      - mountPath: /var/lib/mysql
        name: site-data
        subPath: mysql
    - name: php
      image: php:7.0-apache
      volumeMounts:
      - mountPath: /var/www/html
        name: site-data
        subPath: html
    volumes:
    - name: site-data
      persistentVolumeClaim:
        claimName: my-lamp-site-data
```
### Using subPath with expanded environment variables 
**FEATURE STATE: Kubernetes v1.17 [stable]**
Use the ``subPathExpr``` field to construct ```subPath``` directory names from downward API environment variables. The subPath and subPathExpr properties are mutually exclusive.

In this example, a ```Pod``` uses ```subPathExpr``` to create a directory ```pod1``` within the ```hostPath``` volume ```/var/log/pods```. The hostPath volume takes the ```Pod``` name from the ```downwardAPI```. The host directory ```/var/log/pods/pod1``` is mounted at ```/logs``` in the container.

```
apiVersion: v1
kind: Pod
metadata:
  name: pod1
spec:
  containers:
  - name: container1
    env:
    - name: POD_NAME
      valueFrom:
        fieldRef:
          apiVersion: v1
          fieldPath: metadata.name
    image: busybox
    command: [ "sh", "-c", "while [ true ]; do echo 'Hello'; sleep 10; done | tee -a /logs/hello.txt" ]
    volumeMounts:
    - name: workdir1
      mountPath: /logs
      subPathExpr: $(POD_NAME)
  restartPolicy: Never
  volumes:
  - name: workdir1
    hostPath:
      path: /var/log/pods
```

## Resources
The storage media (such as Disk or SSD) of an emptyDir volume is determined by the medium of the filesystem holding the kubelet root dir (typically /var/lib/kubelet). There is no limit on how much space an emptyDir or hostPath volume can consume, and no isolation between containers or between pods.

To learn about requesting space using a resource specification, see how to manage resources






