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

    $scope.createSneaker = function(selectedSneaker) {
        // console.log("In submit")
        // console.log("selectedAlbum = ", selectedAlbum)
        // console.log("selectedCloset = ", selectedCloset)
        console.log("selectedSneaker = ", selectedSneaker)
        result = {"name": `${selectedSneaker.name}`,
                  "closet": `${selectedSneaker.closet}`,
                  "brand": `${selectedSneaker.brand}`,
                  "images": null,
                  "release_date": `${selectedSneaker.release_date}`,
                  "purchase_date": `${selectedSneaker.purchase_date}`,
                  "retail_price": `${selectedSneaker.retail_price}`,
                  "resale_value": `${selectedSneaker.resale_value}`}

            // "name": null,
            // "closet": "http://localhost:8000/deadstox/closets/1/",
            // "images": "http://localhost:8000/deadstox/sneakers/classnotes3.jpg",
            // "brand": "Nike",
            // "release_date": "2016-09-24T06:00:00Z",
            // "purchase_date": "2016-09-24T12:00:00Z",
            // "retail_price": "$120.00",
            // "resale_value": "$1,000.00"

        NewItemFactory.postNewSneaker(result)
    }


    $scope.createCloset = function(selectedCloset) {
        // console.log("In submit")
        console.log("selectedCloset = ", selectedCloset)
        result = {"name": `${selectedCloset.name}`,
                  "sneakers": null,
                 }
        NewItemFactory.postNewCloset(result)
    }

            // "name": "The Kloset",
            // "total_retail_value": "$6,435.98",
            // "total_resale_value": "$8,726.37",
            // "total_profit": "$2,290.39",

    const edit = this;

    edit.root = null;

    edit.sneakerdetail = null;



    const errorHandle = (e) => console.log(e);

    RootFactory.getRoot()
      .then((root) => {
        edit.root = root;
        return $http.get(`${edit.root.sneakers}`);
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




