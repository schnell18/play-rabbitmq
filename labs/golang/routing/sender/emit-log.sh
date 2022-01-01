for i in {1..2000}; do
    if [[ $(($i % 3)) == 0 ]]; then
        ./emit_log "info" "task[$i]" $(printf '=%.0s' $(seq 1 $(($i % 5))))
    fi
    if [[ $(($i % 3)) == 1 ]]; then
        ./emit_log "warn" "task[$i]" $(printf '=%.0s' $(seq 1 $(($i % 5))))
    else
        ./emit_log "error" "task[$i]" $(printf '=%.0s' $(seq 1 $(($i % 5))))
    fi
done
