'use strict';

/* Controllers */

angular.module('restApp.controllers', [])
    .controller('ItemsController', ['$scope', 'Item', function($scope, Item) {
        // Get items from db
        $scope.items = Item.query();
    }]); 