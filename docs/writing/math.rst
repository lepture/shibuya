:description: Shibuya sphinx theme displays math pretty well.

Math
====

Here shows the results of math rendering.

Inline math
-----------

.. code-block:: none

    Here is an equation: :math:`(a + b)^2 = a^2 + 2ab + b^2`.

Here is an equation: :math:`(a + b)^2 = a^2 + 2ab + b^2`.


Block math
----------

.. code-block:: none

    .. math::
        :label: block math label

        (a + b)^2 = a^2 + 2ab + b^2

        (a - b)^2 = a^2 - 2ab + b^2

.. math::
    :label: block math label

    (a + b)^2 = a^2 + 2ab + b^2

    (a - b)^2 = a^2 - 2ab + b^2

.. code-block:: none

    .. math::
        :nowrap:

        \begin{eqnarray}
            y    & = & ax^2 + bx + c \\
            f(x) & = & x^2 + 2xy + y^2
        \end{eqnarray}

.. math::
    :nowrap:

    \begin{eqnarray}
        y    & = & ax^2 + bx + c \\
        f(x) & = & x^2 + 2xy + y^2
    \end{eqnarray}
