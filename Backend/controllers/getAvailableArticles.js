const Post = require("../models/availablePost") ;

// Get all available articles -verified-
const getAvailableArticles = async (req, res) => {
   try {
      const posts = await Post.find();
      res.status(200).json(posts)
   } catch(err) {
      res.status(404).json({});
   }
};

module.exports=getAvailableArticles;
