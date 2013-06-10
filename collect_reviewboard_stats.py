from reviewboard_client import ReviewboardClient

def collect_reviewboard_stats(reviewboard_url, usernames):
	reviewboard_client = ReviewboardClient.create_using_reviewboard_url(reviewboard_url)
	return dict(
		(
			username,
			reviewboard_client.get_review_requests(username)
		) for username in usernames
	)
