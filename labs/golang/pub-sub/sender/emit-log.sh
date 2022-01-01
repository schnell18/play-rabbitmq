for i in {1..2000}; do
    ./emit_log "task[$i]" $(printf '=%.0s' $(seq 1 $(($i % 5))))
done
