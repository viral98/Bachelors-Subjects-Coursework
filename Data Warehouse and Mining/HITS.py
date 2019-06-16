from math import sqrt
def compute_hits(n, max_iter, hubs, auth, tol):
	prevhubs = [0 for i in range(n)]
	prevauth = [0 for i in range(n)]

	for i in range(max_iter):
		prevauth=sum(auth)
		prevhubs=sum(hubs)

		auth = [0 for i in range(n)]

		for i in range(n):
			for j in range(n):
				if G[i][j] == 1:
					auth[i]+=hubs[j]

		auth_scale = sqrt(sum([x**2 for x in auth]))


		hubs = [0 for i in range(n)]

		for i in range(n):
			for j in range(n):
				if G[i][j] == 1:
					hubs[i]+=auth[j]

		hub_scale = sqrt(sum([x**2 for x in hubs]))


		auth = [x/auth_scale for x in auth]
		hubs = [x/hub_scale for x in hubs]

		if abs(sum(hubs) - prevhubs) < n*tol or abs(sum(auth)-prevauth) < n*tol:
			break
	return hubs, auth

G = []
n = int(input("Enter number of pages"))
print("Enter Adjacency matrix")

for i in range(n):
	d = list(map(int,input('Enter row')))
	G.append(d)

max_iter = 3
tol = 1e-6
hubs = [1 for i in range(n)]
auth = [1 for i in range(n)]

print(compute_hits(n,max_iter,hubs,auth,tol))