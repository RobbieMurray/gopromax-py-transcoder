# Project spec

- creation of a Git Repo (eg on Github.com, but can provide a private repo if required), that will host code, and the basic readme wiki, and have an appropriate licence (such as GPL v2 or BSD)
- Cross platform compatibility (Windows, MacOS, Linux)
- only uses public domain information, ref source of such in comments / attributions
- only uses licence free libs / 3rd party (except ignore any licence issues w.r.t codec)
- has a debug option at run time that monitors relative performance of operation

Phased functionality development (first 2 min phases below)

Phase 1 - preparing the files for further processing

- take command line params for input (and output) file names
- evaluates if input file is a valid file, else returns an error (example " not a video file" or "not a RAW GoPro Max file etc")
- strips out the files into several base files (namely the relevant meta data, 2 x video streams)

Phase 2 - parsing the metadata

- take command line params for input file name
- evaluates if input file is a valid 360 metadata file, else returns an error
- reports for each frame the 3 rotations to reorientate the frame to match the camera pose of the first frame
- optionally (command line option at launch) performs the rotations w.r.t grid north, level horizon (aka zero roll / pitch)

# Init outline + links

the ["official public"](https://github.com/gopro/gpmf-parser)

And

Ffmpeg for stream extraction and the v360 filter for doing video projection transformation.

And

[This very relevant public blog post from GoPro.](https://gopro.com/en/us/news/max-tech-specs-stitching-resolution)

And then have a look at sample file from your buddy

X
XXXX
x

^ then think about this cube unfolding and look at the projection they use to understand how it's saved as a video file

That should give you some background on this.

The bearing angles w.r.t. start frame, and just doing a simple crop (ffmpeg and or opencv) for the 2 files.

Aim is to do an element of a stabilizing and reorientation of the video without using the GoPro player app. To a licence free open source python3 code.
