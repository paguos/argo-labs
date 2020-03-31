#!/usr/bin/env bash
set -eu -o pipefail

killall kubectl || true

info() {
    echo '[INFO] ' "$@"
}

info "argo on http://localhost:2747"
kubectl -n argo port-forward service/argo-server 2746:2746 &

info "postgres on http://localhost:5433"
kubectl -n argo port-forward services/postgres 5433:5432 &

info "minio on http://localhost:9000"
kubectl -n argo port-forward service/minio 9000:9000
