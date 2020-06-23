pragma solidity ^0.4.25;

contract Shareport {

address writer;
address buyer;
uint score;
string text;
uint storedData;

struct report {
    address writer;
    address buyer;
    string text;
    uint score;
}

// array of reports
report[] public reports;

    function setReview (address _writer, address _buyer, string _text, uint _score) {
        reports.push(
            report({
                writer: _writer,
                buyer: _buyer,
                text: _text,
                score: _score
            })
        );
    }
        
    function set(uint x) {
        storedData = x;
    }

    function get() constant returns (uint) {
        return storedData;
    }

}
