const resource = fetchProfileData()

function ProfilePage() {
  return (
    <Suspense fallback={<h1>Loading Profile...</h1>}>
      <ProfileDetails />
      <Suspense fallback={<h1>Loading posts...</h1>}>
        <ProfileTimeline />
      </Suspense>
    </Suspense>
  )
}
// 


function ProfileDetails() {
  const user = resource.user.read()

  return (
    <h1>
      {user.name}
    </h1>
  )
}
// read user from resource and print the profile

function ProfileTimeline() {
  const posts = resource.posts.read()

  return (
    <ul>
      {posts.map(post => (
        <li key={post.id}>{post.text}</li>
      ))}
    </ul>
  )
}
// have a component that renders the posts that is read with resource