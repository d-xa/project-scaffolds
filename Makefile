subdir-to-branch:
	wget -O - https://raw.githubusercontent.com/d-xa/scripts/master/subdir_to_branch.sh | bash -s update -b=$b -r=https://github.com/d-xa/project-scaffolds.git -y
	git checkout main