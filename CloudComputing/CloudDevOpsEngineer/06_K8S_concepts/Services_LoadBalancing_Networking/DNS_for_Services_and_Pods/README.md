# DNS for Services and Pods
Kubernetes creates DNS records for services and pods. You can contact services with consistent DNS names instead of IP addresses.

## Introduction
Kubernetes DNS schedules a DNS Pod and Service on the cluster, and configures the kubelets to tell individual containers to use the DNS Service's IP to resolve DNS names.

Every Service defined in the cluster (including the DNS server itself) is assigned a DNS name. By default, a client Pod's DNS search list includes the Pod's own namespace and the cluster's default domain.

### Namespaces of Services

A DNS query may return different results based on the namespace of the pod making it. DNS queries that don't specify a namespace are limited to the pod's namespace. Access services in other namespaces by specifying it in the DNS query.

For example, consider a pod in a ```test``` namespace. A ```data``` service is in the prod namespace.

A query for ```data``` returns no results, because it uses the pod's test namespace.

A query for ```data.prod``` returns the intended result, because it specifies the namespace.

DNS queries may be expanded using the pod's /etc/resolv.conf. Kubelet sets this file for each pod. For example, a query for just data may be expanded to data.test.svc.cluster.local. The values of the search option are used to expand queries. To learn more about DNS queries, see the ```resolv.conf``` manual page.

```
nameserver 10.32.0.10
search <namespace>.svc.cluster.local svc.cluster.local cluster.local
options ndots:5
```

In summary, a pod in the test namespace can successfully resolve either ```data.prod``` or ```data.prod.svc.cluster.local```.

### DNS Records
What objects get DNS records?

- 1.Services
- 2.Pods
The following sections detail the supported DNS record types and layout that is supported. Any other layout or names or queries that happen to work are considered implementation details and are subject to change without warning. For more up-to-date specification, see Kubernetes DNS-Based Service Discovery.


## Services
## A/AAAA records
- "Normal" (not headless) Services are assigned a DNS A or AAAA record, depending on the IP family of the service, for a name of the form ```my-svc.my-namespace.svc.cluster-domain.example```. This resolves to the cluster IP of the Service.

- "Headless" (without a cluster IP) Services are also assigned a DNS A or AAAA record, depending on the IP family of the service, for a name of the form my-svc.my-namespace.svc.cluster-domain.example. Unlike normal Services, this resolves to the set of IPs of the pods selected by the Service. Clients are expected to consume the set or else use standard round-robin selection from the set.

### SRV records
SRV Records are created for named ports that are part of normal or Headless Services. For each named port, the SRV record would have the form _my-port-name._my-port-protocol.my-svc.my-namespace.svc.cluster-domain.example. For a regular service, this resolves to the port number and the domain name: my-svc.my-namespace.svc.cluster-domain.example. For a headless service, this resolves to multiple answers, one for each pod that is backing the service, and contains the port number and the domain name of the pod of the form auto-generated-name.my-svc.my-namespace.svc.cluster-domain.example.
