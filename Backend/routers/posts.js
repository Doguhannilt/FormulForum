const express = require("express")

// Routes
const getArticles = require("../controllers/getArticles");
const postArticles = require("../controllers/postArticles");
const getAvailableArticles = require("../controllers/getAvailableArticles")

const router = express.Router();

// Routers
router.get("/",getArticles);
router.post("/",postArticles);
router.get("/current",getAvailableArticles)

module.exports=router
