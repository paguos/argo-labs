.PHONY: clean
clean:
	kubectl delete ns argo
	kubectl delete ns argo-events

.PHONY: install
install:
	kubectl create ns argo
	kubectl -n argo apply -f https://raw.githubusercontent.com/argoproj/argo/master/manifests/quick-start-postgres.yaml
	kubectl create ns argo-events
	kubectl -n argo-events apply -f https://raw.githubusercontent.com/argoproj/argo-events/master/hack/k8s/manifests/installation.yaml
	kubectl apply -n argo-events -f kubernetes/argo-events/clusterrole.yml
	kubectl apply -n argo-events -f kubernetes/argo-events/crb.yml

.PHONY: pf
pf:
	./scripts/port_forward.sh

## Additional Commands

.PHONY: hello-world
hello-world:
	argo submit https://raw.githubusercontent.com/argoproj/argo/master/examples/hello-world.yaml -n argo --serviceaccount=argo

.PHONY: cron
cron:
	kubectl apply -n argo -f kubernetes/workflows/cron.yml

.PHONY: events
events:
	kubectl -n argo-events apply -f kubernetes/argo-events/examples/resources/event.yml
	kubectl -n argo-events apply -f kubernetes/argo-events/examples/resources/gateway.yml
	kubectl -n argo-events apply -f kubernetes/argo-events/examples/resources/sensor.yml

.PHONY: workflows
workflows:
	# Submit Workflow A
	argo submit kubernetes/workflows/source_a.yml

	# Submit Workflow B
	argo submit kubernetes/workflows/source_b.yml

