## How to run
You could revise the prompt as you want
### LLaMA2-7b
```torchrun llama-2.py```
### LLaMA2-13B
You must add the param `--nproc_per_node 2`
```torchrun --nproc_per_node 2 llama-2-13b.py```

### falcon-7b
```python falcon-7b.py```