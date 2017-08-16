# The following sudo commands are used to install BareCTF
# When these commands are executed, barectf v2.2.1 is installed with five includable configuration # files:
#
#	std.int.yaml
#	stdfloat.yaml
#	stdmisc.yaml
#	lttng-ust-log-levels.yaml
#	trace-basic.yaml
#
#For more documentation, please refer to https://github/efficios/barectf/wiki/Including-external-#YAML-files

sudo pacman -S python-pip
sudo pip install barectf
