#!/usr/bin/node
exports.callMeMoby = function (x, theFunction) {
    let result = [];
    for (let i = 0; i < x; i++) {
        result.push(theFunction());
    }
    return result;
}
