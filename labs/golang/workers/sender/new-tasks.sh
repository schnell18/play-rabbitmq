for i in {1..20}; do
    ./new_task "task[$i]" $(printf '=%.0s' $(seq 1 $(($i % 5))))
done
