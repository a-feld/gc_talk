Garbage Collection
------------------

This repository contains a collection of scripts meant to aid in finding and
debugging reference cycles in Python.

Contents
--------
`gc_talk/pytest_gc.py`: A pytest fixture to fail your test if your test contains a reference cycle.

`gc_talk/debug.py`: Edit this file to create a graph of a reference cycle. This
is useful for tracking down and debugging a cycle.
