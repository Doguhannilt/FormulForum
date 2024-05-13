const Post = require("../models/availablePost")

// Get all informations given by client-side and save it
const postArticles = async (req, res) => {
    try {
        const posts = new Post({
            id: req.body.id,
            title: req.body.title,
            text: req.body.text,
            date: req.body.date,
            mail: req.body.mail,
            name: req.body.name,
            username: req.body.username,
        });
        await posts.save();
        res.json(posts);
    } catch (err) {
        res.status(500).json({error:err.message});
    }
}

module.exports=postArticles
