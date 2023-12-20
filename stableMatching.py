def stable_matching(mPref, wPref):
    mRet = {man: None for man in mPref}
    womRet = {woman: None for woman in wPref}
    wPref_ranked = {woman: {man: i for i, man in enumerate(preferences)} for woman, preferences in wPref.items()}

    while None in mRet.values():
        for man, curWom in mRet.items():
            if curWom is None:
                women_ranked = wPref_ranked[man]
                for woman in mPref[man]:
                    if womRet[woman] is None:
                        mRet[man] = woman
                        womRet[woman] = man
                        break
                    elif women_ranked[woman] < women_ranked[womRet[woman]]:
                        mRet[womRet[woman]] = None
                        mRet[man] = woman
                        womRet[woman] = man
                        break

    return mRet

mPref = {
    'M1': ['W1', 'W2', 'W3'],
    'M2': ['W2', 'W1', 'W3'],
    'M3': ['W1', 'W3', 'W2']
}
wPref = {
    'W1': ['M1', 'M2', 'M3'],
    'W2': ['M2', 'M1', 'M3'],
    'W3': ['M1', 'M3', 'M2']
}
result = stable_matching(mPref, wPref)
print("Stable Matching Result:")
for man, woman in result.items():
    print(f"{man} is engaged to {woman}")
