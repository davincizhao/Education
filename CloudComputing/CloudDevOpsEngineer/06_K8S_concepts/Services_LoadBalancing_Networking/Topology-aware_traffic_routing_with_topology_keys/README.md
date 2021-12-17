# Topology-aware traffic routing with topology keys
**FEATURE STATE:** Kubernetes v1.21 **[deprecated]**


**Note:** This feature, specifically the alpha topologyKeys API, is deprecated since Kubernetes v1.21. Topology Aware Hints, introduced in Kubernetes v1.21, provide similar functionality.


%%Service Topology%% enables a service to route traffic based upon the Node topology of the cluster. For example, a service can specify that traffic be preferentially routed to endpoints that are on the same Node as the client, or in the same availability zone.

## Topology-aware traffic routing
By default, traffic sent to a ClusterIP or NodePort Service may be routed to any backend address for the Service. Kubernetes 1.7 made it possible to route "external" traffic to the Pods running on the same Node that received the traffic. For ClusterIP Services, the equivalent same-node preference for routing wasn't possible; nor could you configure your cluster to favor routing to endpoints within the same zone. By setting topologyKeys on a Service, you're able to define a policy for routing traffic based upon the Node labels for the originating and destination Nodes.

The label matching between the source and destination lets you, as a cluster operator, designate sets of Nodes that are "closer" and "farther" from one another. You can define labels to represent whatever metric makes sense for your own requirements. In public clouds, for example, you might prefer to keep network traffic within the same zone, because interzonal traffic has a cost associated with it (and intrazonal traffic typically does not). Other common needs include being able to route traffic to a local Pod managed by a DaemonSet, or directing traffic to Nodes connected to the same top-of-rack switch for the lowest latency.

## Using Service Topology
If your cluster has the ServiceTopology feature gate enabled, you can control Service traffic routing by specifying the topologyKeys field on the Service spec. This field is a preference-order list of Node labels which will be used to sort endpoints when accessing this Service. Traffic will be directed to a Node whose value for the first label matches the originating Node's value for that label. If there is no backend for the Service on a matching Node, then the second label will be considered, and so forth, until no labels remain.

If no match is found, the traffic will be rejected, as if there were no backends for the Service at all. That is, endpoints are chosen based on the first topology key with available backends. If this field is specified and all entries have no backends that match the topology of the client, the service has no backends for that client and connections should fail. The special value "*" may be used to mean "any topology". This catch-all value, if used, only makes sense as the last value in the list.


## Examples
The following are common examples of using the Service Topology feature.

### Only Node Local Endpoints
A Service that only routes to node local endpoints. If no endpoints exist on the node, traffic is dropped:
```
apiVersion: v1
kind: Service
metadata:
  name: my-service
spec:
  selector:
    app: my-app
  ports:
    - protocol: TCP
      port: 80
      targetPort: 9376
  topologyKeys:
    - "kubernetes.io/hostname"
```
