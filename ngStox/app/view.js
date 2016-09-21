angular.module("NgStox")

  .controller("View", function($scope, $http, $timeout, $rootScope, RootFactory) {

    $scope.currentCloset;
    $scope.closets = [];
    const errorHandle = (e) => console.log(e);

    $scope.displayClosetChoice = function(closet) {
      console.log("closet is", closet);
      $scope.currentCloset = closet
      // $http.get("http://localhost:8000/closets/", closet)
    }

    // Populate closet data.
    $scope.loadPage = () => {
      RootFactory.getRoot()
        .then((root) => {
          $http.get(root.closets)
              .then((closetslist) => {
                $scope.closets = closetslist.data.results;
                $timeout();
              }, errorHandle);
          return root;
        }, errorHandle)
        .then((root) => {
          $http.get(root.sneakers)
              .then((sneakerslist) => {
                $scope.sneakers = sneakerslist.data.results;
                $timeout();
              }, errorHandle);
          return root;
        }, errorHandle)
        // .then((root) => {
        //   $http.get(root.albums)
        //       .then((albumslist) => {
        //         $scope.albums = albumslist.data;
        //         $timeout();
        //       }, errorHandle);
        // });
    };
   // Call populate closets data on page load.
    $scope.loadPage();

    // $scope.openModal = (songId) => {
    //   //opens a modal to view details of the song clicked.
    //   const modalInstance = $uibModal.open({
    //     size: "lg",
    //     templateUrl: "app/modal.html",
    //     controller: "Modal",

    //     controllerAs: "modal",
    //     resolve: {
    //       'songId': songId
    //     }
    //   });
    // };

    //fancy listener to reload the page when someone edits/deletes a sneaker from the closet.
    $rootScope.$on("reloadPagePlease", () => {
      $scope.loadPage();
    });

  //   $scope.sum = function (num1, num2) {
  //     $scope.subtraction = parseInt(num1) - parseInt(num2);
  //   }
  // })

    $scope.filterSongsByArtist = function (selectedArtist) {
      /*
        1. We've got the artist selected
        2. Look at albums that have the artist
        3. Then filter tracks that are on those albums
      */
      $scope.filteredSongs = $scope.songs.filter((song) => {
        return song.artist === song.artists.name
      });

      $scope.filteredSongs = filter;
        /*
          1. Determine which artist is selected
          2. Grab its ID
          3. Iterate over all tracks and find which ones are by the selected artist
          4. Put those into the $scope.filteredSongs collection
        */

        // $scope.filteredSongs = $scope.songs

        // $scope.filteredSongs = [];

        // $scope.songFilter = $scope.filteredSongs[0].id

    }

  });

