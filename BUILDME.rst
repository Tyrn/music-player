Music Player
************

Peniel's Player for Linux and Android

Development
===========

- `Buildozer <https://github.com/kivy/buildozer>`__
- `KivyMD <https://github.com/kivymd/KivyMD>`__; MDDropdownMenu `1 <https://github.com/kivymd/KivyMD/issues/1203>`__, `2 <https://stackoverflow.com/questions/71510107/kivymd-update-mddropdownmenu-open-generates-an-error>`__
- `Kivy Garden <https://github.com/kivy-garden>`__

Use Git Hooks
-------------

::

    (.venv) $ pre-commit install
    ...
    (.venv) $ pre-commit run --all-files

Poetry (Desktop)
----------------

::

    $ poetry install
    $ poetry shell
    (.venv) $ python music_player/main.py

Check memory usage
^^^^^^^^^^^^^^^^^^

::

    (.venv) $ mprof run -C python music_player/main.py
    ...
    (.venv) $ mprof plot -o profile_.png

Buildozer (Mobile)
------------------

- `Build Docker Image <https://github.com/kivy/buildozer#buildozer-docker-image>`__

::

    $ docker-compose run buildozer android [debug | release]
    $ adb install -r bin/*.apk

*NB*, 2022-11-26: The above works for ``debug`` only. ``release`` requires explicit signing.
