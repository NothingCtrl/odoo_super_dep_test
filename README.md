# Odoo `super` dependency test

This module to test how Odoo process python `super` call with module dependency


## Dependency Structure

```
mod_a
    |--> mod_a1 --> mod_a11
    |--> mod_b1 --> mod_b11 --> mod_b111
        |--> mod_a1b1 (depends on mod_a1, mod_b1)

```

### Test install and logs

#### Install test 1

* mod_a
* mod_a1
* mod_b1
* mod_a11
* mod_b11
* mod_b111
* mod_a1b1

Application logs after install all modules

```
(older)
=== [CREATE] Demo Model in module mod_a1b1 run ===
=== [CREATE] Demo Model in module mod_b111 run ===
=== [CREATE] Demo Model in module mod_b11 run ===
=== [CREATE] Demo Model in module mod_a11 run ===
=== [CREATE] Demo Model in module mod_b1 run ===
=== [CREATE] Demo Model in module mod_a1 run ===
=== [CREATE] Demo Model in module mod_a run ===
...
...
=== [WRITE] Demo Model in module mod_a1b1 run ===
=== [WRITE] Demo Model in module mod_b111 run ===
=== [WRITE] Demo Model in module mod_b11 run ===
=== [WRITE] Demo Model in module mod_a11 run ===
=== [WRITE] Demo Model in module mod_b1 run ===
=== [WRITE] Demo Model in module mod_a1 run ===
=== [WRITE] Demo Model in module mod_a run ===
...
...
=== [UNLINK] Demo Model in module mod_a1b1 run ===
=== [UNLINK] Demo Model in module mod_b111 run ===
=== [UNLINK] Demo Model in module mod_b11 run ===
=== [UNLINK] Demo Model in module mod_a11 run ===
=== [UNLINK] Demo Model in module mod_b1 run ===
=== [UNLINK] Demo Model in module mod_a1 run ===
=== [UNLINK] Demo Model in module mod_a run ===
(newer)
```

#### Install test 2

Install modules:

* mod_b111
* mod_a11

Application logs after install above modules:

```
(older)
=== [CREATE] Demo Model in module mod_a11 run ===
=== [CREATE] Demo Model in module mod_a1 run ===
=== [CREATE] Demo Model in module mod_b111 run ===
=== [CREATE] Demo Model in module mod_b11 run ===
=== [CREATE] Demo Model in module mod_b1 run ===
=== [CREATE] Demo Model in module mod_a run ===
...
...
=== [WRITE] Demo Model in module mod_a11 run ===
=== [WRITE] Demo Model in module mod_a1 run ===
=== [WRITE] Demo Model in module mod_b111 run ===
=== [WRITE] Demo Model in module mod_b11 run ===
=== [WRITE] Demo Model in module mod_b1 run ===
=== [WRITE] Demo Model in module mod_a run ===
...
...
=== [UNLINK] Demo Model in module mod_a11 run ===
=== [UNLINK] Demo Model in module mod_a1 run ===
=== [UNLINK] Demo Model in module mod_b111 run ===
=== [UNLINK] Demo Model in module mod_b11 run ===
=== [UNLINK] Demo Model in module mod_b1 run ===
=== [UNLINK] Demo Model in module mod_a run ===
(newer)
```

Next, install module:

* mod_a1b1

Application logs after install above modules

```
(older)
=== [CREATE] Demo Model in module mod_a1b1 run ===
=== [CREATE] Demo Model in module mod_b111 run ===
=== [CREATE] Demo Model in module mod_b11 run ===
=== [CREATE] Demo Model in module mod_a11 run ===
=== [CREATE] Demo Model in module mod_b1 run ===
=== [CREATE] Demo Model in module mod_a1 run ===
=== [CREATE] Demo Model in module mod_a run ===
...
...
=== [WRITE] Demo Model in module mod_a1b1 run ===
=== [WRITE] Demo Model in module mod_b111 run ===
=== [WRITE] Demo Model in module mod_b11 run ===
=== [WRITE] Demo Model in module mod_a11 run ===
=== [WRITE] Demo Model in module mod_b1 run ===
=== [WRITE] Demo Model in module mod_a1 run ===
=== [WRITE] Demo Model in module mod_a run ===
...
...
=== [UNLINK] Demo Model in module mod_a1b1 run ===
=== [UNLINK] Demo Model in module mod_b111 run ===
=== [UNLINK] Demo Model in module mod_b11 run ===
=== [UNLINK] Demo Model in module mod_a11 run ===
=== [UNLINK] Demo Model in module mod_b1 run ===
=== [UNLINK] Demo Model in module mod_a1 run ===
=== [UNLINK] Demo Model in module mod_a run ===
(newer)
```

#### Install test 3

Install modules:

* mod_a1b1
* mod_a11

Application logs after install above modules:

```
(older)
=== [CREATE] Demo Model in module mod_a11 run ===
=== [CREATE] Demo Model in module mod_a1b1 run ===
=== [CREATE] Demo Model in module mod_b1 run ===
=== [CREATE] Demo Model in module mod_a1 run ===
=== [CREATE] Demo Model in module mod_a run ===
...
...
=== [WRITE] Demo Model in module mod_a11 run ===
=== [WRITE] Demo Model in module mod_a1b1 run ===
=== [WRITE] Demo Model in module mod_b1 run ===
=== [WRITE] Demo Model in module mod_a1 run ===
=== [WRITE] Demo Model in module mod_a run ===
...
...
=== [UNLINK] Demo Model in module mod_a11 run ===
=== [UNLINK] Demo Model in module mod_a1b1 run ===
=== [UNLINK] Demo Model in module mod_b1 run ===
=== [UNLINK] Demo Model in module mod_a1 run ===
=== [UNLINK] Demo Model in module mod_a run ===
(newer)
```

Next, install module:

* mod_b111

Application logs after install above modules:

```
(older)
=== [CREATE] Demo Model in module mod_b111 run ===
=== [CREATE] Demo Model in module mod_b11 run ===
=== [CREATE] Demo Model in module mod_a1b1 run ===
=== [CREATE] Demo Model in module mod_a11 run ===
=== [CREATE] Demo Model in module mod_b1 run ===
=== [CREATE] Demo Model in module mod_a1 run ===
=== [CREATE] Demo Model in module mod_a run ===
...
...
=== [WRITE] Demo Model in module mod_b111 run ===
=== [WRITE] Demo Model in module mod_b11 run ===
=== [WRITE] Demo Model in module mod_a1b1 run ===
=== [WRITE] Demo Model in module mod_a11 run ===
=== [WRITE] Demo Model in module mod_b1 run ===
=== [WRITE] Demo Model in module mod_a1 run ===
=== [WRITE] Demo Model in module mod_a run ===
...
...
=== [UNLINK] Demo Model in module mod_b111 run ===
=== [UNLINK] Demo Model in module mod_b11 run ===
=== [UNLINK] Demo Model in module mod_a1b1 run ===
=== [UNLINK] Demo Model in module mod_a11 run ===
=== [UNLINK] Demo Model in module mod_b1 run ===
=== [UNLINK] Demo Model in module mod_a1 run ===
=== [UNLINK] Demo Model in module mod_a run ===
(newer)
```