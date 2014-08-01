all: addons

design/gym.xmi: design/gym.zargo
	-echo "REBUILD gym.xmi from gym.zargo. I cant do it"

addons: gym

gym: design/gym.uml
	xmi2oerp -r -i $< -t addons -v 2

clean:
	rm -rf addons/gym/*
	sleep 1
	touch design/gym.uml
