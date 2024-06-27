const express = require("express")
const { getUsers, getUsersById, getUsersByEmail } = require("../controllers/getUsers");

const router = express.Router();

//router.get("/",getUsers)
router.get("/id/:id",getUsersById)
router.get("/email/:email",getUsersByEmail)


module.exports=router