import cx_Freeze as cx

executables=[cx.Executable("Covid19_The_Game.py")]

cx.setup(
    name='Covid19',
    options={"build_exe":{"packages":["pygame"],"include_files":["Covid_19.bmp","Evil Incoming.mp3","USSR.mp3",
                "combined_worldmap_wc_3800.png","Covid_scientist.bmp"]}},
    description="Covid19 the pandemic's game",
    executables=executables


)