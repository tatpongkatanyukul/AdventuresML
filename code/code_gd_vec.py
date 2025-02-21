step_size = 0.4
Nmax = 1000
tol = 1e-6
v = np.array([[2.5], [3.5]]) 

losses = []
gradv = grad(v)
for i in range(Nmax):
    v = v - step_size * gradv
    gradv = grad(v)
    loss = g(v)
    losses.append(loss)

    eps = np.linalg.norm(gradv)
    if  eps <= tol:
        print('Terminate at i={} with {}'.format(i,eps))
        break

    print('{}: v= [{:.3f} {:.3f}]; grad = [{:.4f} {:.4f}]'.format(i,v[0,0],v[1,0],gradv[0,0],gradv[1,0]))

print('{}: v= [{} {}]; g = {}'.format(i,v[0,0],v[1,0],loss))
