/**
 * Created by Simon on 2015/12/8.
 */
var supertest = require ( "supertest" ) ;

var should = require ( "should" ) ;

// This agent refers to PORT where program is runninng.

var server = supertest. agent ( "http://localhost:8080" ) ;

// UNIT test begin

describe ( "BillList" , function ( ) {

// #1 should return home page

    it ( "should return home page" , function ( done ) {

// calling home page api

        server

            . get ( "/healthmanager/rest/bill/list" )

            . expect ( "Content-type" ,/ json / )

            . expect ( 200 ) // THis is HTTP response

            . end ( function ( err , res ) {

// HTTP status should be 200

            res. status.should . equal ( 200 ) ;

// Error key should be false.

            res. body.error.should.equal ( false ) ;

            done ( ) ;

        } ) ;

    } ) ;

} )
;