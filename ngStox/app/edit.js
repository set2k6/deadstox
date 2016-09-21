angular.module("NgStox")
  .controller("Edit", function($scope, $http, $timeout, RootFactory, NewItemFactory) {
    $scope.title = "Closet and Sneaker Additions";

    RootFactory.getSneakers()
    .then((sneakers) => {
        $scope.sneakersList = sneakers
        console.log("$scope.sneakersList = ", $scope.sneakersList)
    }).then(
        RootFactory.getClosets().then((closets) => {
            $scope.closetList = closets
            console.log("$scope.closetList = ", $scope.closetList)
            // })(
        //         RootFactory.getArtists().then((artists) => {
        //             $scope.artistList = artists
        //             console.log("$scope.artistList = ", $scope.artistList)
            })
        // )
    ).then($timeout())

    $scope.createSneaker = function(selectedSneaker, selectedCloset) {
        // console.log("In submit")
        // console.log("selectedAlbum = ", selectedAlbum)
        console.log("selectedCloset = ", selectedCloset)
        result = {"name": "${selectedSneaker}","Closets": ["${selectedCloset}"]}
        NewItemFactory.postNewSneaker(result)
    }


    // $scope.createArtist = function(selectedArtist) {
    //     // console.log("In submit")
    //     // console.log("selectedAlbum = ", selectedAlbum)
    //     result = `{"name": "${selectedArtist}"}`
    //     NewItemFactory.postNewArtist(result)
    // }


    $scope.createCloset = function(selectedCloset) {
        // console.log("In submit")
        console.log("selectedSneaker = ", selectedSneaker)
        result = `{"name": "${selectedCloset}"}`
        NewItemFactory.postNewCloset(result)
    }


    const edit = this;

    edit.root = null;

    edit.sneakerdetail = null;



    const errorHandle = (e) => console.log(e);

    RootFactory.getRoot()
      .then((root) => {
        edit.root = root;
        return $http.get(`${edit.root.sneakers}${sneakersId}`);
      }, errorHandle)
      .then((sneakerdetail) => {
        edit.sneakerdetail = sneakerdetail.data;
        console.log(" sneaker detail", edit.sneakerdetail );
        $timeout();
      })
      .then(() => {
        return $http.get(`${edit.root.closets}`);
        // return RootFactory.getAlbums();
      }, errorHandle)
      .then((closets) => {
        console.log("closets", closets.data);
        edit.closets = closets.data;
        $timeout();
      });



    edit.change = function () {
      //update selected song information.
      return $http.put(`${edit.sneakerdetail.url}`, edit.sneakerdetail)
        .then(()=> {
          $scope.$emit("reloadPagePlease");
        }, errorHandle)
        // .then(()=> {
        //   $uibModalInstance.close();
        // });
    };

    edit.delete = function () {
      //deletes selected song.
      return $http.delete(`${edit.sneakerdetail.url}`)
      .then(()=> {
        $scope.$emit("reloadPagePlease");
      }, errorHandle)
      // .then(()=> {
      //   $uibModalInstance.close();
      // });
    };


  });




