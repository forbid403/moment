
/**
 * 데이터베이스 사용하기
 * 
 * 데이터베이스 열고 로그인 화면에 붙이기
 * 
 */

//===== 모듈 불러들이기 =====//
var express = require('express')
  , http = require('http')
  , path = require('path');
var cors = require('cors')
var bodyParser = require('body-parser');
var cookieParser = require('cookie-parser');
var expressSession = require('express-session');
var expressErrorHandler = require('express-error-handler');
var request = require('request');
var favicon = require('serve-favicon')
var url = require('url');
var fs = require('fs');

//===== MySQL 데이터베이스를 사용할 수 있도록 하는 mysql 모듈 불러오기 =====//
var mongoose = require('mongoose');
//===== MySQL 데이터베이스 연결 설정 =====//
var db = mongoose.connection;
db.on('error', console.error);
db.once('open', function(){
    // CONNECTED TO MONGODB SERVER
    console.log("Connected to mongod server");
});
mongoose.connect('mongodb://moment:moment2019@168.131.30.129:27017/moment');

var Schema = mongoose.Schema;

const articlesSchema = new Schema({
	title : String,
	provider : String,
	category : [String],
	incidents : [String],
	location : String,
	time : {type : Date},
	id : Schema.Types.ObjectId
});

var Articles = mongoose.model('articles',articlesSchema);

//===== Express 서버 객체 만들기 =====//
var app = express();


//===== 서버 변수 설정 및 static으로 public 폴더 설정  =====//
app.set('port', process.env.PORT || 3000);

app.use(express.static('views'));
app.use(favicon(path.join(__dirname,'views/images','moment.ico')))
app.use(bodyParser.urlencoded({extended: true}));
app.use(bodyParser.json());
app.set("view engine", "ejs");
app.use(cookieParser());

app.use(expressSession({
	secret:'my key',
	resave:true,
	saveUninitialized:true
}));
app.use(cors());

//===== 라우터 미들웨어 사용 =====//
app.get('/', function(req, res) {
	let user = req.session.user;
	var notice;
	console.log("메인 페이지 시랳ㅇ");
			if(req.url == '/'){
				res.render('front', {"user" : user,"notice" : notice});	
			}
			if(req.url == '/favicon.ico'){
				return response.writeHead(404);
			}
	
	
	console.log(notice)
	//req.session.user.id"";
	console.log(user);
	
});

app.post('/process/front',function(req,res){
	res.redirect('/');
});

app.post('/ajax_send_db',function(req,res){
	if(req.body.location == "대한민국"){
		Articles.find({},function(err,result){
			if(err){
				return;
			}
			res.send(result);
		});
		return;
	};
	var location = req.body.location;
	console.log(location);
	Articles.find({category : { $in : [location]}},function(err,result){
		if(err){
			return;
		}
		console.log(result);
		res.send(result);
	}).limit(200);
});

app.post('/ajax_send_api',function(req, res){
	console.log(req.body);
	var country = req.body.country;
	var api_url = 'https://newsapi.org/v2/top-headlines?' +
	'country=' + country +
	'&apiKey=f8b6710e4fac4d37b44169b23758efe4';
	request(api_url,function(err,response,body){
		res.send(body)
	})
})

//===== 404 에러 페이지 처리 =====//
var errorHandler = expressErrorHandler({
 static: {
   '404': './404.html'
 }
});

app.use( expressErrorHandler.httpError(404) );
app.use( errorHandler );

//===== 서버 시작 =====//
http.createServer(app).listen(app.get('port'), function(){
  console.log('서버가 시작되었습니다. 포트 : ' + app.get('port'));
});
