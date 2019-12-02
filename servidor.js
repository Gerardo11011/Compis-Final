const express = require('express')
const router = express.Router()
const cors = require('cors')
var fs = require('fs');
var exec = require('child_process').exec;

function execute(command, callback){
    exec(command, function(error, stdout, stderr){ callback(stdout); });
};


var compile = function(req, res){
  fs.writeFile('Pruebas/idecode.txt', req.body.data, function (err) {
    if (err){res.send("ERROR")};
  });
  execute("python yacc.py", function(compilation){
    res.send({"response": compilation})
  });
}


router.all('*', cors());
router.post('/compile', compile);
router.post('/testing', function(req, res){res.send("YEI, SI JALA")})
router.get('*', function(req, res) {
  res.send({
    error: 'route does not exist'
  })
})

const app = express()
const port = 3000

app.use(express.json())
app.use(router)

app.listen(port, function(){
  console.log("running");
})
