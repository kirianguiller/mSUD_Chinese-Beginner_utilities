# Useful Grew commands
## Rewrite
### permute 好<-吃 to 好->吃 (and derivations)
```
rule r1 {
 pattern { N [form="好", upos="ADJ"] ; e: M-[mod]->N; M[upos=VERB]}
  commands { 
	del_edge e; % delete the edge
    shift M ==> N;
    add_edge N -[mod]-> M;
	}
}
```
