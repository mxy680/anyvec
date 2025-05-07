Installation
============

To install **anyvec**, use pip (or poetry):

.. code-block:: bash

   pip install anyvec

Docker Image
============

You can skip building locally and pull the latest public image directly from Docker Hub:

.. code-block:: bash

   docker pull mxy680/clip-inference:latest

Then run the container:

.. code-block:: bash

   docker run --rm -it -p 8000:8080 mxy680/clip-inference:latest

The API will be available at http://localhost:8000