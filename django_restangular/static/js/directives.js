'use strict';

/* Directives */

angular.module('restApp.directives', [])
    .directive('itemlist', ['Item', function(Item) {
        return {
            restrict : 'E',
            templateUrl : '/static/templates/item_list.html',
            scope : {
                group_name : '@groupName',
                can_add : '=canAdd',
                items : '=items',
            },
            controller : function($scope, $element, $attrs) {
                /*
                 * Create item
                 */
                $scope.createItem = function(item_name) {
                    if (item_name && $scope.can_add) {
                        var new_item = {
                            name : item_name
                        };
                        Item.save(new_item, function(saved_item) {
                            $scope.items.push(saved_item);
                        });
                        $scope.new_item_name = '';
                    }
                }
                
                /*
                 * Delete item
                 */
                $scope.deleteItem = function(item) {
                    Item.remove({
                        itemId : item.id
                    });
                    $scope.items.splice($scope.items.indexOf(item), 1);
                }
            }
        }
    }]);
