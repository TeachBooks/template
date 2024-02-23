# Including a code block and a figure

Here is a code block that is parsed from a python file:

```{eval-rst}
.. literalinclude:: ../code/sinewave.py
   :language: python
```

Which is the result of:

    ```{eval-rst}
    .. literalinclude:: sinewave.py
       :language: python
    ```

We can toggle the code block by nesting it inside a `toggle` directive:

    ```{toggle}
    ```{eval-rst}
    .. literalinclude:: sinewave.py
       :language: python
    ```

Note the single `-triplet at the end of the toggle.

````{toggle}
```{eval-rst}
.. literalinclude:: ../code/sinewave.py
   :language: python
```
````

The Python file saves the figure, so we can include it using the regular markdown recipe:


```{figure} ../figures/sinewave.svg
---
name: sine_wave
---
A sine wave
```

```{figure} ../figures/cosinewave.svg
---
name: cosine_wave
---
A cosine wave
```