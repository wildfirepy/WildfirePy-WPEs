# WildfirePy-WPEs

## WildfirePy Proposals for Enhancement

WPEs are documents used to address non-trivial major enhancements that require sustained discussion and thoughtful consideration beyond what is typically covered by a single Pull Request. These proposals are meant to reflect some current or emergent need of the `WildfirePy` community, to keep the community's work and output relevant and timely. Normally a proposal would go through various phases of the WPE lifecycle. Discussions are expected to be carried out using existing mechanisms (via GitHub, Riot IRC, etc), and eventually, a decision would be settled upon regarding whether the proposal would be modified and either accepted or rejected.

## Proposing a new WPE

New WPEs should be created using the `WPE-template.rst` file in this repository. Please fork the repository, copy `WPE-template.rst` to `WPE_<some_working_name>.rst` and open a Pull Request to add that file in this repository once you've written up the WPE (a little explanation is required in the PR itself given that the document has all the self-explanatory content - usually it's easiest to just paste the abstract to the PR description). The WPE number will be assigned once the PR is merged.

Note that there is not sufficient ground for making proposals unless someone or some group has signed up to implement it once the WPE is accepted (typically this would involve the author or authors of the WPE). Just submitting a WPE to spur others to do work is not the expected practice. Generally, an implementation should have been begun before a WPE can be considered fully accepted. For proposals that require extensive follow-up work that few are willing to commit, provisional acceptance is an option. For serious consideration, it is usually a good idea to show that detailed technical aspects have been covered with real code samples.

## Finalizing the WPEs

The final decision on accepting or rejecting proposed WPEs lies with the `WildfirePy` community. Once the community discussion on the WPE has come to a close, the group shall commence discussion of the concerned WPE and make a final decision on either its eventual acceptance or rejection. One of the group members should then carry out the following steps accordingly:

1. Fill in the "Decision rationale" section of the WPE with a description of why the WPE was accepted or rejected, concluding with a summary of the community's discussion as required.

2. Update the "date-last-revised" to the day of merging and "status" to either "Accepted" or "Rejected".

3. If necessary, rename the WPE file to be `WPE_##.rst`, where `##` is the next free number on the list of WPEs.

4. Leave a brief comment in the PR indicating the result.

5. Merge the PR with the above changes.

6. If the WPE has been accepted then continue with the remaining steps, otherwise stop now:

7. Upload Zenodo to include the WPE to give the Zenodo record a DOI.

8. Get the source for the DOI badge from the newly-created Zenodo record page by clicking on the DOI badge on the right side of the page and copying the entire reStructuredText source.

9. On GitHub (or locally) edit `README.md` and add an entry for the new EPE to the "Accepted WPEs" table. Use the DOI link from the previous step. Add corresponding MD link refs for both the DOI link and the new WPE. Preview the update and test the links to make sure they are all correct. Then ask someone with push access to the repository to review the final PR.

10. Send an email to the `WildfilePy` community's mailing list announcing the acceptance. In general, this should just point to the accepted WPE rather than providing additional decision rationale in support of its acceptance or rejection.

## Updating the WPEs

In the cases where an updated WPE requires revision (e.g. references to a new WPE that supersedes it, clarifying information that emerges after the WPE is accepted, etc.), changes can be made directly via PR, but the "date-last-revised" should be updated in the WPE also. Additionally, the corresponding Zenodo entry will need to be updated with a new version of the WPE (but not with a completely new Zenodo entry), by using the "New version" button and then filling out the forms as described above.

## Accepted WPEs

| \#  | Title | Date | DOI |
| :-: | :---: | :--: | :-: |
