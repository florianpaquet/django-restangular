'use strict';

/* Services */

angular.module('restApp.services', ['ngResource'])
    .factory('Item', function($resource) {
        return $resource('http://localhost\\:8000/items/:itemId');
    });
