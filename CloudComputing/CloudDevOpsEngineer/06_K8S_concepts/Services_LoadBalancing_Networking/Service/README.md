# Service
An abstract way to expose an application running on a set of Pods as a network service.
With Kubernetes you don't need to modify your application to use an unfamiliar service discovery mechanism. Kubernetes gives Pods their own IP addresses and a single DNS name for a set of Pods, and can load-balance across them.

## Motivation
Kubernetes Pods are created and destroyed to match the state of your cluster. Pods are nonpermanent resources. If you use a Deployment to run your app, it can create and destroy Pods dynamically.

Each Pod gets its own IP address, however in a Deployment, the set of Pods running in one moment in time could be different from the set of Pods running that application a moment later.

This leads to a problem: if some set of Pods (call them "backends") provides functionality to other Pods (call them "frontends") inside your cluster, how do the frontends find out and keep track of which IP address to connect to, so that the frontend can use the backend part of the workload?


## Service resources
In Kubernetes, a Service is an abstraction which defines a logical set of Pods and a policy by which to access them (sometimes this pattern is called a micro-service). The set of Pods targeted by a Service is usually determined by a selector. To learn about other ways to define Service endpoints, see Services without selectors.

For example, consider a stateless image-processing backend which is running with 3 replicas. Those replicas are fungible—frontends do not care which backend they use. While the actual Pods that compose the backend set may change, the frontend clients should not need to be aware of that, nor should they need to keep track of the set of backends themselves.

The Service abstraction enables this decoupling.

### Cloud-native service discovery
If you're able to use Kubernetes APIs for service discovery in your application, you can query the API server for Endpoints, that get updated whenever the set of Pods in a Service changes.

For non-native applications, Kubernetes offers ways to place a network port or load balancer in between your application and the backend Pods.

## Defining a Service
A Service in Kubernetes is a REST object, similar to a Pod. Like all of the REST objects, you can POST a Service definition to the API server to create a new instance. The name of a Service object must be a valid RFC 1035 label name.

For example, suppose you have a set of Pods where each listens on TCP port 9376 and contains a label ```app=MyApp```:

```
apiVersion: v1
kind: Service
metadata:
  name: my-service
spec:
  selector:
    app: MyApp
  ports:
    - protocol: TCP
      port: 80
      targetPort: 9376
```
This specification creates a new Service object named "my-service", which targets TCP port 9376 on any Pod with the ```app=MyApp``` label.

Kubernetes assigns this Service an IP address (sometimes called the "cluster IP"), which is used by the Service proxies (see Virtual IPs and service proxies below).

The controller for the Service selector continuously scans for Pods that match its selector, and then POSTs any updates to an Endpoint object also named "my-service".

Port definitions in Pods have names, and you can reference these names in the targetPort attribute of a Service. This works even if there is a mixture of Pods in the Service using a single configured name, with the same network protocol available via different port numbers. This offers a lot of flexibility for deploying and evolving your Services. For example, you can change the port numbers that Pods expose in the next version of your backend software, without breaking clients.

The default protocol for Services is TCP; you can also use any other supported protocol.

As many Services need to expose more than one port, Kubernetes supports multiple port definitions on a Service object. Each port definition can have the same protocol, or a different one.

### Services without selectors
Services most commonly abstract access to Kubernetes Pods, but they can also abstract other kinds of backends. For example:

- You want to have an external database cluster in production, but in your test environment you use your own databases.
- You want to point your Service to a Service in a different Namespace or on another cluster.
- You are migrating a workload to Kubernetes. While evaluating the approach, you run only a portion of your backends in Kubernetes.
In any of these scenarios you can define a Service without a Pod selector. For example:
```
apiVersion: v1
kind: Service
metadata:
  name: my-service
spec:
  ports:
    - protocol: TCP
      port: 80
      targetPort: 9376      
```

Because this Service has no selector, the corresponding Endpoints object is not created automatically. You can manually map the Service to the network address and port where it's running, by adding an Endpoints object manually:

```
apiVersion: v1
kind: Endpoints
metadata:
  name: my-service
subsets:
  - addresses:
      - ip: 192.0.2.42
    ports:
      - port: 9376
```
The name of the Endpoints object must be a valid DNS subdomain name.

**Note:**
The endpoint IPs must not be: ```loopback (127.0.0.0/8 for IPv4, ::1/128 for IPv6)```, or link-local ```(169.254.0.0/16 and 224.0.0.0/24 for IPv4, fe80::/64 for IPv6)```.

Endpoint IP addresses cannot be the cluster IPs of other Kubernetes Services, because kube-proxy doesn't support virtual IPs as a destination.

Accessing a Service without a selector works the same as if it had a selector. In the example above, traffic is routed to the single endpoint defined in the ```YAML: 192.0.2.42:9376 (TCP)``` .

**Note:** The Kubernetes API server does not allow proxying to endpoints that are not mapped to pods. Actions such as ```kubectl proxy <service-name>``` where the service has no selector will fail due to this constraint. This prevents the Kubernetes API server from being used as a proxy to endpoints the caller may not be authorized to access.
An ExternalName Service is a special case of Service that does not have selectors and uses DNS names instead. For more information, see the ExternalName section later in this document.
  
### Over Capacity Endpoints
If an Endpoints resource has more than 1000 endpoints then a Kubernetes v1.22 (or later) cluster annotates that Endpoints with endpoints.kubernetes.io/over-capacity: truncated. This annotation indicates that the affected Endpoints object is over capacity and that the endpoints controller has truncated the number of endpoints to 1000.
  
### EndpointSlices
**FEATURE STATE: Kubernetes v1.21 [stable]**
EndpointSlices are an API resource that can provide a more scalable alternative to Endpoints. Although conceptually quite similar to Endpoints, EndpointSlices allow for distributing network endpoints across multiple resources. By default, an EndpointSlice is considered "full" once it reaches 100 endpoints, at which point additional EndpointSlices will be created to store any additional endpoints.

EndpointSlices provide additional attributes and functionality which is described in detail in EndpointSlices.

### Application protocol
**FEATURE STATE: Kubernetes v1.20 [stable]**
The appProtocol field provides a way to specify an application protocol for each Service port. The value of this field is mirrored by the corresponding Endpoints and EndpointSlice objects.

This field follows standard Kubernetes label syntax. Values should either be IANA standard service names or domain prefixed names such as ```mycompany.com/my-custom-protocol```  

## Virtual IPs and service proxies
Every node in a Kubernetes cluster runs a kube-proxy. kube-proxy is responsible for implementing a form of virtual IP for Services of type other than ExternalName.

### Why not use round-robin DNS?
A question that pops up every now and then is why Kubernetes relies on proxying to forward inbound traffic to backends. What about other approaches? For example, would it be possible to configure DNS records that have multiple A values (or AAAA for IPv6), and rely on round-robin name resolution?

There are a few reasons for using proxying for Services:

- There is a long history of DNS implementations not respecting record TTLs, and caching the results of name lookups after they should have expired.
- Some apps do DNS lookups only once and cache the results indefinitely.
- Even if apps and libraries did proper re-resolution, the low or zero TTLs on the DNS records could impose a high load on DNS that then becomes difficult to manage.

Later in this page you can read about various kube-proxy implementations work. Overall, you should note that, when running kube-proxy, kernel level rules may be modified (for example, iptables rules might get created), which won't get cleaned up, in some cases until you reboot. Thus, running kube-proxy is something that should only be done by an administrator which understands the consequences of having a low level, privileged network proxying service on a computer. Although the kube-proxy executable supports a cleanup function, this function is not an official feature and thus is only available to use as-is.

### Configuration
Note that the kube-proxy starts up in different modes, which are determined by its configuration.

- The kube-proxy's configuration is done via a ConfigMap, and the ConfigMap for kube-proxy effectively deprecates the behaviour for almost all of the flags for the kube-proxy.
- The ConfigMap for the kube-proxy does not support live reloading of configuration.
- The ConfigMap parameters for the kube-proxy cannot all be validated and verified on startup. For example, if your operating system doesn't allow you to run iptables commands, the standard kernel kube-proxy implementation will not work. Likewise, if you have an operating system which doesn't support netsh, it will not run in Windows userspace mode.
### User space proxy mode
In this (legacy) mode, kube-proxy watches the Kubernetes control plane for the addition and removal of Service and Endpoint objects. For each Service it opens a port (randomly chosen) on the local node. Any connections to this "proxy port" are proxied to one of the Service's backend Pods (as reported via Endpoints). kube-proxy takes the SessionAffinity setting of the Service into account when deciding which backend Pod to use.

Lastly, the user-space proxy installs iptables rules which capture traffic to the Service's ```clusterIP``` (which is virtual) and ```port```. The rules redirect that traffic to the proxy port which proxies the backend Pod.

By default, kube-proxy in userspace mode chooses a backend via a round-robin algorithm.
![services-userspace-overview](https://d33wubrfki0l68.cloudfront.net/e351b830334b8622a700a8da6568cb081c464a9b/13020/images/docs/services-userspace-overview.svg)

### iptables proxy mode
In this mode, kube-proxy watches the Kubernetes control plane for the addition and removal of Service and Endpoint objects. For each Service, it installs iptables rules, which capture traffic to the Service's ```clusterIP``` and ```port```, and redirect that traffic to one of the Service's backend sets. For each Endpoint object, it installs iptables rules which select a backend Pod.

By default, kube-proxy in iptables mode chooses a backend at random.

Using iptables to handle traffic has a lower system overhead, because traffic is handled by Linux netfilter without the need to switch between userspace and the kernel space. This approach is also likely to be more reliable.

If kube-proxy is running in iptables mode and the first Pod that's selected does not respond, the connection fails. This is different from userspace mode: in that scenario, kube-proxy would detect that the connection to the first Pod had failed and would automatically retry with a different backend Pod.

You can use Pod readiness probes to verify that backend Pods are working OK, so that kube-proxy in iptables mode only sees backends that test out as healthy. Doing this means you avoid having traffic sent via kube-proxy to a Pod that's known to have failed.

![services-iptables-overview](https://d33wubrfki0l68.cloudfront.net/27b2978647a8d7bdc2a96b213f0c0d3242ef9ce0/e8c9b/images/docs/services-iptables-overview.svg)

### IPVS proxy mode
**FEATURE STATE: Kubernetes v1.11 [stable]**
In ```ipvs``` mode, kube-proxy watches Kubernetes Services and Endpoints, calls ```netlink``` interface to create IPVS rules accordingly and synchronizes IPVS rules with Kubernetes Services and Endpoints periodically. This control loop ensures that IPVS status matches the desired state. When accessing a Service, IPVS directs traffic to one of the backend Pods.

The IPVS proxy mode is based on netfilter hook function that is similar to iptables mode, but uses a hash table as the underlying data structure and works in the kernel space. That means kube-proxy in IPVS mode redirects traffic with lower latency than kube-proxy in iptables mode, with much better performance when synchronising proxy rules. Compared to the other proxy modes, IPVS mode also supports a higher throughput of network traffic.

IPVS provides more options for balancing traffic to backend Pods; these are:

- ```rr```: round-robin
- ```lc```: least connection (smallest number of open connections)
- ```dh```: destination hashing
- ```sh```: source hashing
- ```sed```: shortest expected delay
- ```nq```: never queue

**Note:**
To run kube-proxy in IPVS mode, you must make IPVS available on the node before starting kube-proxy.

When kube-proxy starts in IPVS proxy mode, it verifies whether IPVS kernel modules are available. If the IPVS kernel modules are not detected, then kube-proxy falls back to running in iptables proxy mode.

![services-ipvs-overview](https://d33wubrfki0l68.cloudfront.net/2d3d2b521cf7f9ff83238218dac1c019c270b1ed/9ac5c/images/docs/services-ipvs-overview.svg)

In these proxy models, the traffic bound for the Service's IP:Port is proxied to an appropriate backend without the clients knowing anything about Kubernetes or Services or Pods.

If you want to make sure that connections from a particular client are passed to the same Pod each time, you can select the session affinity based on the client's IP addresses by setting ```service.spec.sessionAffinity``` to "ClientIP" (the default is "None"). You can also set the maximum session sticky time by setting ```service.spec.sessionAffinityConfig.clientIP.timeoutSeconds``` appropriately. (the default value is 10800, which works out to be 3 hours).

## Multi-Port Services
For some Services, you need to expose more than one port. Kubernetes lets you configure multiple port definitions on a Service object. When using multiple ports for a Service, you must give all of your ports names so that these are unambiguous. For example:
```
apiVersion: v1
kind: Service
metadata:
  name: my-service
spec:
  selector:
    app: MyApp
  ports:
    - name: http
      protocol: TCP
      port: 80
      targetPort: 9376
    - name: https
      protocol: TCP
      port: 443
      targetPort: 9377
```
**Note:**
As with Kubernetes names in general, names for ports must only contain lowercase alphanumeric characters and -. Port names must also start and end with an alphanumeric character.

For example, the names 123-abc and web are valid, but 123_abc and -web are not.

## Choosing your own IP address
You can specify your own cluster IP address as part of a ```Service``` creation request. To do this, set the ```.spec.clusterIP``` field. For example, if you already have an existing DNS entry that you wish to reuse, or legacy systems that are configured for a specific IP address and difficult to re-configure.

The IP address that you choose must be a valid IPv4 or IPv6 address from within the ```service-cluster-ip-range``` CIDR range that is configured for the API server. If you try to create a Service with an invalid clusterIP address value, the API server will return a 422 HTTP status code to indicate that there's a problem.

## Traffic policies
### External traffic policy
You can set the ```spec.externalTrafficPolicy``` field to control how traffic from external sources is routed. Valid values are ```Cluster``` and ```Local```. Set the field to ```Cluster``` to route external traffic to all ready endpoints and ```Local``` to only route to ready node-local endpoints. If the traffic policy is Local and there are are no node-local endpoints, the kube-proxy does not forward any traffic for the relevant Service.

**Note:**
**FEATURE STATE: Kubernetes v1.22 [alpha]**
If you enable the ProxyTerminatingEndpoints feature gate for the kube-proxy, the kube-proxy checks if the node has local endpoints and whether or not all the local endpoints are marked as terminating. If there are local endpoints and all of those are terminating, then the kube-proxy ignores any external traffic policy of Local. Instead, whilst the node-local endpoints remain as all terminating, the kube-proxy forwards traffic for that Service to healthy endpoints elsewhere, as if the external traffic policy were set to Cluster. This forwarding behavior for terminating endpoints exists to allow external load balancers to gracefully drain connections that are backed by NodePort Services, even when the health check node port starts to fail. Otherwise, traffic can be lost between the time a node is still in the node pool of a load balancer and traffic is being dropped during the termination period of a pod.

### Internal traffic policy
FEATURE STATE: Kubernetes v1.22 [beta]
You can set the spec.internalTrafficPolicy field to control how traffic from internal sources is routed. Valid values are Cluster and Local. Set the field to Cluster to route internal traffic to all ready endpoints and Local to only route to ready node-local endpoints. If the traffic policy is Local and there are no node-local endpoints, traffic is dropped by kube-proxy.



## Discovering services
Kubernetes supports 2 primary modes of finding a Service 
- environment variables 
- DNS.

### Environment variables
When a Pod is run on a Node, the kubelet adds a set of environment variables for each active Service. It supports both Docker links compatible variables (see makeLinkVariables) and simpler ```{SVCNAME}_SERVICE_HOST``` and ```{SVCNAME}_SERVICE_PORT``` variables, where the Service name is upper-cased and dashes are converted to underscores.

For example, the Service ```redis-master``` which exposes TCP port 6379 and has been allocated cluster IP address 10.0.0.11, produces the following environment variables:
```
REDIS_MASTER_SERVICE_HOST=10.0.0.11
REDIS_MASTER_SERVICE_PORT=6379
REDIS_MASTER_PORT=tcp://10.0.0.11:6379
REDIS_MASTER_PORT_6379_TCP=tcp://10.0.0.11:6379
REDIS_MASTER_PORT_6379_TCP_PROTO=tcp
REDIS_MASTER_PORT_6379_TCP_PORT=6379
REDIS_MASTER_PORT_6379_TCP_ADDR=10.0.0.11
```

**Note:**
When you have a Pod that needs to access a Service, and you are using the environment variable method to publish the port and cluster IP to the client Pods, you must create the Service before the client Pods come into existence. Otherwise, those client Pods won't have their environment variables populated.

If you only use DNS to discover the cluster IP for a Service, you don't need to worry about this ordering issue.

### DNS
You can (and almost always should) set up a DNS service for your Kubernetes cluster using an add-on.

A cluster-aware DNS server, such as CoreDNS, watches the Kubernetes API for new Services and creates a set of DNS records for each one. If DNS has been enabled throughout your cluster then all Pods should automatically be able to resolve Services by their DNS name.

For example, if you have a Service called ```my-service``` in a Kubernetes namespace ```my-ns```, the control plane and the DNS Service acting together create a DNS record for ```my-service.my-ns```. Pods in the my-ns namespace should be able to find the service by doing a name lookup for ```my-service``` (```my-service.my-ns``` would also work).

Pods in other namespaces must qualify the name as ```my-service.my-ns```. These names will resolve to the cluster IP assigned for the Service.

Kubernetes also supports DNS SRV (Service) records for named ports. If the my-service.my-ns Service has a port named http with the protocol set to ```TCP```, you can do a DNS SRV query for ```_http._tcp.my-service.my-ns``` to discover the port number for ```http```, as well as the IP address.

The Kubernetes DNS server is the only way to access ```ExternalName``` Services. You can find more information about ```ExternalName``` resolution in DNS Pods and Services.

## Headless Services
Sometimes you don't need load-balancing and a single Service IP. In this case, you can create what are termed "headless" Services, by explicitly specifying "None" for the cluster IP (.spec.clusterIP).

You can use a headless Service to interface with other service discovery mechanisms, without being tied to Kubernetes' implementation.

For headless ```Services```, a cluster IP is not allocated, kube-proxy does not handle these Services, and there is no load balancing or proxying done by the platform for them. How DNS is automatically configured depends on whether the Service has selectors defined:

### With selectors
For headless Services that define selectors, the endpoints controller creates Endpoints records in the API, and modifies the DNS configuration to return A records (IP addresses) that point directly to the ```Pods``` backing the ```Service```.

### Without selectors
For headless Services that do not define selectors, the endpoints controller does not create ```Endpoints``` records. However, the DNS system looks for and configures either:

- CNAME records for ExternalName-type Services.
- A records for any ```Endpoints``` that share a name with the Service, for all other types.

