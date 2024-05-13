const Post = require("../models/posts") ;

// Get "all" articles
const getArticles = async (req, res) => {
   try {
      const posts = await Post.find();
      res.status(200).json(posts)
   } catch(err) {
      res.status(404).json({message: "Invalid Credentials"});
      console.log(err)
   }
};

module.exports=getArticles;
