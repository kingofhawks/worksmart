/**
 * Created by Simon on 2015/12/8.
 */
var supertest = require("supertest") ;
var should = require("should") ;

// This agent refers to PORT where program is running
var server = supertest.agent( "http://localhost:8080" ) ;

describe ( "BillList" , function ( ) {
    it ( "should return list of Bill" , function ( done ) {
// calling bill list API
        server
            . get ( "/healthmanager/rest/bill/list" )
            . expect ( "Content-type" ,/ json / )
            . expect ( 200 )
            . end ( function ( err , res ) {
                console.log(res);
                res. status.should . equal ( 200 ) ;
                res. body.error.should.equal ( false ) ;
                done ( ) ;
            } ) ;
    } ) ;
} );


describe ( "BillFields" , function ( ) {
    it ( "should return fields of Bill" , function ( done ) {
// calling bill fields API
        server
            . get ( "/healthmanager/rest/bill/fields" )
            . expect ( "Content-type" ,/ json / )
            . expect ( 200 )
            . end ( function ( err , res ) {
                console.log(res);
                res. status.should . equal ( 200 ) ;
                res. body.error.should.equal ( false ) ;
                done ( ) ;
            } ) ;
    } ) ;
} );

describe ( "CreateBill" , function ( ) {
    it ( "should create Bill" , function ( done ) {
// calling create bill API
        server
            .post( "/healthmanager/rest/bill/create" )
            .set('Content-Type', 'multipart/form-data')
            //.set('Content-Type', 'application/x-www-form-urlencoded')
            .send({"FPicName":"test"})
            . expect ( "Content-type" ,/ json / )
            . expect ( 200 )
            . end ( function ( err , res ) {
                console.log(res);
                res. status.should . equal ( 200 ) ;
                res. body.error.should.equal ( false ) ;
                done ( ) ;
            } ) ;
    } ) ;
} );