// Libraries
const express = require("express")
const bodyParser = require("body-parser")
const mongoose = require("mongoose")
const dotenv = require("dotenv")
const cors = require("cors")
const { expressjwt: jwt } = require("express-jwt");
const jwks = require("jwks-rsa")

// Routers
const postRouters = require("./routers/posts")
const signupRouter = require("./routers/signup")
const userRouter = require("./routers/users")


// Ports and Express
const auth = require("./middlewares/auth")
const PORT =process.env.PORT || 5000;
const app = express();

// Dotenv
dotenv.config()

// BodyParser and Cors
app.use(bodyParser.json())
app.use(bodyParser.urlencoded({extended:true}))
app.use(cors())

// Routers
app.use("/protected",signupRouter) 
console.log("signupRouter has been working on protected URL")
app.use("/post",postRouter);
console.log("postRouter has been working on postRouter URL")
app.use("/user",userRouter);
// MONGODB 
mongoose
.connect(process.env.CONNECTION_URL,
    { useNewUrlParser: true, 
      useUnifiedTopology: true ,
})
.then(()=>{
    app.listen(5000,()=>{
        console.log(`Server is running on port ${PORT}`)
        })
})
.catch((error)=>{
    console.error(error);
});



