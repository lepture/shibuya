:description: Shibuya sphinx theme displays math pretty well.

Math
====


Inline math
-----------

Here is an equation:
:math:`(a + b)^2 = a^2 + 2ab + b^2`.


Block math
----------

.. math::
   :label: block math label

   (a + b)^2 = a^2 + 2ab + b^2

   (a - b)^2 = a^2 - 2ab + b^2

.. math::
   :nowrap:

   \begin{eqnarray}
      y    & = & ax^2 + bx + c \\
      f(x) & = & x^2 + 2xy + y^2
   \end{eqnarray}
