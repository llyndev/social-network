import { Fetcher } from "../fetcher.js"
import { Post } from "./post.js"

export const ListPosts = async () => {

    const response = await Fetcher({
        url: '/posts/all-posts',
        method: 'GET'
    });

    const listPostPromises = response.users.map(async (user) => await Post(user));
    const listUsers = await Promise.all(listPostPromises);

    return `
        <section class="list-post">${
            listUsers.join('')
        }</section>
    `
}