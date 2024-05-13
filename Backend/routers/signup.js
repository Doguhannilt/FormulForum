const express = require("express")
const auth = require("../middlewares/auth")

// Routes
const signup = require("../controllers/signup")
const router = express.Router();

router.use(auth)

// Router
router.get("/",signup)

module.exports=router
