INSTALLED=$(cat ~/.zprofile | grep PROFILE_REPO_DIR | wc -l)

echo "installed '$INSTALLED'"

if [ $INSTALLED -ne '       0' ]; then
  echo "It's already installed"
else
  echo "Installing"
  echo "#Terminal Profile" >> ~/.zprofile
  echo "PROFILE_REPO_DIR=`pwd`" >> ~/.zprofile
  echo 'source $PROFILE_REPO_DIR/.profile' >> ~/.zprofile
fi

