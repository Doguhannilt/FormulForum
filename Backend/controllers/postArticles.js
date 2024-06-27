const Post = require("../models/availablePost")
const articleCounter = require("./articleCounter");
// Get all informations given by client-side and save it
const postArticles = async (req, res) => {
    try {
        const posts = new Post({
            userId:req.body.userId,
            title: req.body.title,
            text: req.body.text,
            date: req.body.date,
            mail: req.body.mail,
            name: req.body.name,
            username: req.body.username,
        });
        await posts.save();
        try {
            await articleCounter(posts.userId);
        } catch (err) {
            console.error('Error updating article count:', err);
            return res.status(500).json({ error: 'Failed to update article count' });
        }
        res.json(posts);
    } catch (err) {
        res.status(500).json({error:err.message});
    }
}

module.exports=postArticles
