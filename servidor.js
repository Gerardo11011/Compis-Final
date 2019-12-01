const express = require('express')
const router = express.Router()
const cors = require('cors')
var fs = require('fs');
var exec = require('child_process').exec;

function execute(command, callback){
    exec(command, function(error, stdout, stderr){ callback(stdout); });
};


var cmd = function(){
  execute("python3 lexPar.py", function(compilation){
    console.log(compilation);
  });
};


var compile = function(req, res){
  fs.writeFile('Pruebas/idecode.txt', req.body.data, function (err) {
    if (err){res.send("BIG ERROR")};
  });
  execute("python yacc.py", function(compilation){
    res.send({"response": compilation})
  });
}


router.all('*', cors());
router.post('/compile', compile);
router.post('/testing', function(req, res){res.send("YEI")})
router.get('*', function(req, res) {
  res.send({
    error: 'This route does not exist... But at least you have internet conecction!'
  })
})

const app = express()
const port = 3000

app.use(express.json())
app.use(router)

app.listen(port, function(){
  console.log("running");
})
