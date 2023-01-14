# screen_pipeline
Create an automatic analysis pipeline based on screen sessions.

# Usage

<pre><code>❯ python pipeline.py -h
</code></pre>

<pre><code>Job Submission Pipeline

optional arguments:
  -h, --help            show this help message and exit
  -i INPUT, --input INPUT
                        Input file
  -fish GW_FISH, --GWFish_folder GW_FISH
                        GWFish analysis folder

</code></pre>

This code asks for an input text file containing the list of the objects. The analysis folder has a default value which can be updated using the corresponding flag.

Here an example:

<pre><code>python pipeline.py -i grbs.txt</code></pre>

Which generates a number of screen sessions as the number of input elements:

<pre><code>❯ screen -ls
There are screens on:
	42516.GRB_session_061217	(Detached)
	42498.GRB_session_090417A	(Detached)
	42506.GRB_session_090515	(Detached)
	42503.GRB_session_060502B	(Detached)
	42521.GRB_session_111117A	(Detached)
	42502.GRB_session_070209	(Detached)
	42511.GRB_session_100206A	(Detached)
	42512.GRB_session_100625A	(Detached)
	42499.GRB_session_100628A	(Detached)
	42519.GRB_session_100117A	(Detached)
10 Sockets in /var/folders/0d/pj6l57_n3131rvssv1hwgdw80000gp/T/.screen.
</code></pre>

Each screen session can be normally resumed with the usual -r flag.

After the analysis script ends the screen session remains alive.