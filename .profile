source $PROFILE_REPO_DIR/git-shortcuts/.bash_profile


alias whatis-my-local-ip='ifconfig | grep 192'

alias pdfunite-custom="gs -q -dNOPAUSE -dBATCH -sDEVICE=pdfwrite -sOutputFile=merged.pdf"

alias shuffle-file="$PROFILE_REPO_DIR/src/python/shuffle-file.py"
alias parse-csv="$PROFILE_REPO_DIR/src/python/parse-csv.py"
alias reg-rename="$PROFILE_REPO_DIR/src/python/reg-rename.py"
