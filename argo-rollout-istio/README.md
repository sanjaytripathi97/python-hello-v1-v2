rollout manager needs to be installed.

oc argo rollouts commands needs to be installed.

for rollout

oc argo rollouts get rollout rollouts-demo --watch

$ oc argo rollouts set image rollouts-demo rollouts-demo=<new-image-name>

$ oc argo rollouts get rollout rollouts-demo

$ oc argo rollouts promote rollouts-demo -n <namespace> 

I think bluegreen deployment is not possble with the istio.

Proof:-
oc explain Rollout.spec.strategy.canary.trafficRouting
~~~
KIND:     Rollout
VERSION:  argoproj.io/v1alpha1

RESOURCE: trafficRouting <Object>

DESCRIPTION:
     <empty>

FIELDS:
   alb	<Object>

   ambassador	<Object>

   apisix	<Object>

   appMesh	<Object>

   istio	<Object>

   managedRoutes	<[]Object>

   nginx	<Object>

   plugins	<>

   smi	<Object>

   traefik	<Object>
~~~

oc explain Rollout.spec.strategy.blueGreen.trafficRouting
~~~
error: field "trafficRouting" does not exist
~~~

oc explain Rollout.spec.strategy.blueGreen
~~~
KIND:     Rollout
VERSION:  argoproj.io/v1alpha1

RESOURCE: blueGreen <Object>

DESCRIPTION:
     <empty>

FIELDS:
   abortScaleDownDelaySeconds	<integer>

   activeMetadata	<Object>

   activeService	<string> -required-

   antiAffinity	<Object>

   autoPromotionEnabled	<boolean>

   autoPromotionSeconds	<integer>

   maxUnavailable	<>

   postPromotionAnalysis	<Object>

   prePromotionAnalysis	<Object>

   previewMetadata	<Object>

   previewReplicaCount	<integer>

   previewService	<string>

   scaleDownDelayRevisionLimit	<integer>

   scaleDownDelaySeconds	<integer>
~~~